# easy ipadapterApplyEncoder

## 节点类型

`easy ipadapterApplyEncoder`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip_vision:CLIP_VISION`（2 次）
- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `image3:IMAGE`（2 次）
- `image4:IMAGE`（2 次）
- `mask1:MASK`（2 次）
- `mask2:MASK`（2 次）
- `mask3:MASK`（2 次）
- `mask4:MASK`（2 次）

## 输出

- `model:MODEL`（2 次）
- `clip_vision:CLIP_VISION`（2 次）
- `ipadapter:IPADAPTER`（2 次）
- `pos_embed:EMBEDS`（2 次）
- `neg_embed:EMBEDS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["COMPOSITION", 3, 0.33000000000000007, 0.33000000000000007, 0.33000000000000007, 1, "concat"]`（1 次）
- `["PLUS FACE (portraits)", 3, 0.7000000000000002, 0.6000000000000001, 0.6000000000000001, 1, "concat"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
