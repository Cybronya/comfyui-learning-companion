# LongCatImageTextToImage

## 节点类型

`LongCatImageTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `longcat_pipeline:LONGCAT_PIPE`（1 次）
- `prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `steps:INT`（1 次）
- `guidance_scale:FLOAT`（1 次）
- `seed:INT`（1 次）
- `enable_cfg_renorm:COMBO`（1 次）
- `enable_prompt_rewrite:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "worst quality, illustration, 3d, 2d, painting, cartoons, sketch", 1536, 1024, 50, 4.5, 922609074673348, "randomize`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
