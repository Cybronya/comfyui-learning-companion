# RH_AlibabaQwenImage30ProTextToImage

## 节点类型

`RH_AlibabaQwenImage30ProTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `negativePrompt:STRING`（2 次）
- `size:COMBO`（2 次）
- `imageNum:COMBO`（2 次）
- `promptExtend:BOOLEAN`（2 次）
- `seed:INT`（2 次）
- `skip_error:BOOLEAN`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a close-up of a woman's foot in sheer black stockings,\nwearing a silver patent leather Louboutin stiletto with a red `（1 次）
- `["一位年轻成年东亚女性站在户外热带城市环境中，半身到大半身竖构图，身体背向镜头约三分之二，头部回转看向镜头，形成自然回眸姿态。她身形纤细修长，肩背线条柔和，皮肤白皙偏暖，保留真实毛孔、细微肌理与自然高光，不要塑料磨皮。她有浓密的深棕色长卷`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
