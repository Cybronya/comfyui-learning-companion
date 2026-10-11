# RH_BytedanceSeedance20GlobalMiniTextToVideo

## 节点类型

`RH_BytedanceSeedance20GlobalMiniTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `resolution:COMBO`（2 次）
- `duration:COMBO`（2 次）
- `generateAudio:BOOLEAN`（2 次）
- `ratio:COMBO`（2 次）
- `returnLastFrame:BOOLEAN`（2 次）
- `seed:INT`（2 次）
- `skip_error:BOOLEAN`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["【全局视觉风格】\n3D 迪士尼/皮克斯动画风格，16:9 画幅，4K 极高画质，电影级柔光与梦幻粒子光效，高帧率动作流畅。\n\n【角色全貌设定】\n一个极具亲和力的 3D Q版卡通小女孩（6岁左右）。\n* 头部：浓密丰盈的梦幻浅紫`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
