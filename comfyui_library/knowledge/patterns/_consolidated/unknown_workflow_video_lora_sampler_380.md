---
name: unknown_workflow_video_lora_sampler_380
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.6165
common_nodes: [AILab_QwenVL, CFGZeroStar, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetNode, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewAny, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [图片生成/反推提示词/video_wan2_2_14B_QwenVL-图片反推-自动提示词_1981728799463227394.json, 图片生成/反推提示词/video_wan2_2_14B_QwenVL-视频反推-自动提示词_1981728832958930946.json, 图片生成/反推提示词/video_wan2_2_14B_qwenvl-video-prompt-video_1981195099193376769.json, 视频生成/图生视频/video_wan2_2_14B_qwenvl-image-prompt-video_1981180403119808514.json, 视频生成/文生视频/Supermate 推荐Qwen3vl视频反推提示+Video_wan2_2_14B视频生成_1982073877964693505.json, 视频生成/文生视频/video_wan2_2_14B_QwenVL-自动提示词_1981726042085826562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_380

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/video_wan2_2_14B_QwenVL-图片反推-自动提示词_1981728799463227394.json、图片生成/反推提示词/video_wan2_2_14B_QwenVL-视频反推-自动提示词_1981728832958930946.json、图片生成/反推提示词/video_wan2_2_14B_qwenvl-video-prompt-video_1981195099193376769.json、视频生成/图生视频/video_wan2_2_14B_qwenvl-image-prompt-video_1981180403119808514.json、视频生成/文生视频/Supermate 推荐Qwen3vl视频反推提示+Video_wan2_2_14B视频生成_1982073877964693505.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 6 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 3/6 个有
- `Int` —— 3/6 个有
- `PrimitiveBoolean` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `easy ifElse` —— 3/6 个有
- `LoadImage` —— 2/6 个有
- `TextBox` —— 2/6 个有
- `JjkText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | lcm | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
