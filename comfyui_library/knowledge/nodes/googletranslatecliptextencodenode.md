# GoogleTranslateCLIPTextEncodeNode

## 节点类型

`GoogleTranslateCLIPTextEncodeNode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）

## 输出

- `CONDITIONING:CONDITIONING`（2 次）
- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "en", false, "Manual Trasnlate", "酷帅都市潮男，22岁，单肩挎黑色机能包，站立霓虹街头，车流光轨穿梭。"]`（1 次）
- `["auto", "en", false, "Manual Trasnlate", "一位美丽都市女子，穿着白色轻纱连衣裙，站在湖岸上。湖边的柳枝随风摆动，湖面铺满翠绿欲滴的莲叶， 粉白相间的荷花绽放，露出嫩黄花蕊；亦有含苞待放的蓓蕾。"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
