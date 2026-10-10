# RH_GeminiOmniFlashTextToVideo

## 节点类型

`RH_GeminiOmniFlashTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `duration:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `aspectRatio:COMBO`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["10秒视频，次世代3D格斗游戏画面，真实游戏实机演示风格，电影级光影，虚幻引擎质感，高帧率动作，清晰UI界面，像一段完整的格斗游戏对战剪辑。\n\n角色1P：Ashen（艾申）\n男性，高大强壮，肌肉紧绷，肤色略带灰白，像从废墟与灰烬中`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
