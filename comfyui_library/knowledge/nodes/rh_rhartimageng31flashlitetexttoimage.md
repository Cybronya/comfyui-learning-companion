# RH_RhartImageNG31FlashLiteTextToImage

## 节点类型

`RH_RhartImageNG31FlashLiteTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `aspectRatio:COMBO`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "9:16", false, 1184457083, "randomize"]`（1 次）
- `["超详细的3D分层纸质动漫海报，从错综复杂的剪纸波浪和漩涡云中浮现的动态动漫英雄，火影忍者中的女性角色，多层阴影盒设计，手工纸雕美学，深维剪纸艺术品，清晰的分层卡片纸纹理，大胆的动作姿势，戏剧性的视角，充满活力的人物色彩与优雅的白纸背景形`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
