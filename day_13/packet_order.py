import ast
from functools import cmp_to_key

sum_ordered_packets = 0
decoder_key = 0

with open('input') as input:
      text = input.read()[:-1]
      packets = text.split('\n\n')
      packets = [packet_pair.split('\n') for packet_pair in packets]
      packets = [[ast.literal_eval(packet) for packet in packet_pair] for packet_pair in packets]

      def compare_packets(A, B):
            if type(A) is list and type(B) is list:
                  for i in range(max(len(A), len(B))):
                        if i >= len(A):
                              return  1
                        elif i >= len(B):
                              return -1
                        item = compare_packets(A[i], B[i])
                        if item != 0:
                              return item
                  return 0
            elif type(A) is int and type(B) is int:
                  return 0 if A == B else (1 if A < B else -1)
            elif type(A) is int:
                  return compare_packets([A], B)
            else:
                  return compare_packets(A, [B])

      sum_ordered_packets = sum([(i+1) for i in range(len(packets)) if compare_packets(*packets[i]) > 0])

      packets = [packet for packet_pair in packets for packet in packet_pair]
      packets += [[[2]], [[6]]]
      packets.sort(key=cmp_to_key(compare_packets), reverse=True)
      decoder_key = (packets.index([[2]])+1) * (packets.index([[6]])+1)


      
with open('output', 'w') as output:
      output.write(str(sum_ordered_packets) + '\n')
      output.write(str(decoder_key) + '\n')