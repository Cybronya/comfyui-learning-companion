# WanVideoTextEncode

## 节点类型

`WanVideoTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `t5:WANTEXTENCODER`（3 次）

## 输出

- `text_embeds:WANVIDEOTEXTEMBEDS`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["high quality nature video featuring a red panda balancing on a bamboo stem while a bird lands on it's head, on the bac`（1 次）
- `["", "bad quality video", true]`（1 次）
- `["best quality video of a handsome boy and a cute girl embrace and kiss,", "bad quality video", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
