# RH_RhartImageNNb21OfficialTextToImage

## 节点类型

`RH_RhartImageNNb21OfficialTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（3 次）
- `prompt:STRING`（3 次）
- `resolution:COMBO`（3 次）
- `aspectRatio:COMBO`（3 次）
- `thinkingLevel:COMBO`（3 次）
- `skip_error:BOOLEAN`（3 次）
- `seed:INT`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["超写实治愈人像摄影，画面主体是一位年轻白人少女，有着柔软的金色短发，头发侧边佩戴淡紫色、鹅黄色、奶白色雏菊组成的小花发饰，身穿米白色露肩荷叶边上衣，衣身带有精致镂空蕾丝花纹，面料轻薄飘逸，通透有垂感。少女双手环抱着一只长毛小猫，小猫底色`（1 次）
- `["", "1k", "1:1", "medium", false, 0, "randomize"]`（1 次）
- `["A low-angle close-up photograph of a vintage retro coin-operated arcade machine outdoors at a carnival on a bright sun`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
