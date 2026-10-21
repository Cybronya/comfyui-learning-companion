# BitDanceTextEncode

## 节点类型

`BitDanceTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `text_encoder:BITDANCE_TEXT_ENCODER`（8 次）
- `model_to_offload:BITDANCE_MODEL`（8 次）
- `positive_prompt:STRING`（8 次）
- `negative_prompt:STRING`（8 次）
- `force_offload:BOOLEAN`（8 次）
- `use_disk_cache:BOOLEAN`（8 次）
- `device:COMBO`（8 次）

## 输出

- `positive:BITDANCE_TEXT_EMBEDS`（8 次）
- `negative:BITDANCE_TEXT_EMBEDS`（8 次）
- `positive_prompt:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", false, false, "gpu"]`（5 次）
- `["一张大师级的户外人像摄影作品，使用 85mm f/1.4 定焦镜头 拍摄，画质极度锐利，焦外虚化柔美。 核心光影与色温布局（Lighting & Color Temperature）： ● 主光（Key Light）： 处于黄金时刻（G`（1 次）
- `["一位美丽的中国女人", "", false, false, "gpu"]`（1 次）
- `["", "低质量，模糊，不符合常理的", false, false, "gpu"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
