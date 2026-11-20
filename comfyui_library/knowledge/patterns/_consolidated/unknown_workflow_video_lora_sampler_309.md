---
name: unknown_workflow_video_lora_sampler_309
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.881556
common_nodes: [BerniniConditioning, CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/Bernini 去字幕_2069319958349312001.json, 平台全量/Bernini 去水印_2072550390398283778.json, 平台全量/Bernini 去除物品_2069319928552972290.json, 平台全量/Bernini 服装替换_2069319883577450497.json, 平台全量/Bernini 视频增添物品_2072553243103809537.json, 平台全量/Bernini 视频换背景_2069319980046438401.json, 平台全量/Bernini 视频编辑_2072564660724916226.json, 平台全量/Bernini 视频编辑_2076877872630947841.json, 视频生成/图生视频/Bernini 角色替换_2069319914443333634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_309

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/Bernini 去字幕_2069319958349312001.json、平台全量/Bernini 去水印_2072550390398283778.json、平台全量/Bernini 去除物品_2069319928552972290.json、平台全量/Bernini 服装替换_2069319883577450497.json、平台全量/Bernini 视频增添物品_2072553243103809537.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `LoadImage` —— 5/9 个有
- `JjkText` —— 3/9 个有
- `SeargePromptCombiner` —— 3/9 个有
- `DF_Text_Box` —— 1/9 个有
- `PreviewAny` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | increment | - | 9 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | res_multistep | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 increment，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
