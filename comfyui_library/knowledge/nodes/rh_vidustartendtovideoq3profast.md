# RH_ViduStartEndToVideoQ3ProFast

## 节点类型

`RH_ViduStartEndToVideoQ3ProFast`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `first_image:IMAGE`（3 次）
- `last_image:IMAGE`（3 次）
- `api_config:RH_OPENAPI_CONFIG`（3 次）
- `prompt:STRING`（3 次）
- `duration:COMBO`（3 次）
- `resolution:COMBO`（3 次）
- `audio:BOOLEAN`（3 次）
- `skip_error:BOOLEAN`（3 次）
- `seed:INT`（3 次）

## 输出

- `video:VIDEO`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一镜到底镜头从高空俯拍缓慢向下推进再平稳抬升机位顺滑过渡至仰拍视角，锁定少女双麻花辫、白丝带、奶白洛丽塔裙、蕾丝中筒袜、玛丽珍鞋与毛绒兔子包造型全程无畸变崩坏，春日蔷薇庭院满地落花，微风拂动发丝裙摆，花瓣树叶轻柔飘动，柔和日光丁达尔光影`（1 次）
- `["一镜到底镜头从高空俯拍缓慢向下推进再平稳抬升机位顺滑过渡至仰拍视角，锁定少女双麻花辫、白丝带、奶白洛丽塔裙、蕾丝中筒袜、玛丽珍鞋与毛绒兔子包造型全程无畸变崩坏，春日蔷薇庭院满地落花，微风拂动发丝裙摆，花瓣树叶轻柔飘动，柔和日光丁达尔光影`（1 次）
- `["一镜到底镜头从高空俯拍缓慢向下推进再平稳抬升机位顺滑过渡至仰拍视角，锁定少女双麻花辫、白丝带、奶白洛丽塔裙、蕾丝中筒袜、玛丽珍鞋与毛绒兔子包造型全程无畸变崩坏，春日蔷薇庭院满地落花，微风拂动发丝裙摆，花瓣树叶轻柔飘动，柔和日光丁达尔光影`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
