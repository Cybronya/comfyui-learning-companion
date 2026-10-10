# RH_Veo3_Text2Video

## 节点类型

`RH_Veo3_Text2Video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt:STRING`（2 次）
- `model:COMBO`（2 次）
- `aspect_ratio:COMBO`（1 次）
- `duration_seconds:COMBO`（1 次）
- `seed:INT`（1 次）
- `api_key:STRING`（1 次）

## 输出

- `video:VIDEO`（2 次）
- `video_url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["The flowing silky blue light band extends in curves and spirals, with smooth and rhythmic lines. The main color is dar`（1 次）
- `["这段视频展示了一个特写镜头下的场景，背景是一个明亮的厨房或工作室。画面中心，一只戴着白手套的手稳稳地扶着一个外观晶莹剔透、如同果冻般的红色火龙果，它被放置在一块木质砧板上。一把锋利的厨刀从上方干脆利落地切下，将火龙果一分为二，露出内部黑`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
