---
name: unknown_workflow_video_lora_sampler_199
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.592222
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetNode, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: [Label (rgthree)]
members: [图片生成/文生图/1953391990853521409.json, 图片生成/文生图/1961428825634750466.json, 图片生成/文生图/1970462683160080385.json, 图片生成/文生图/1989283451264225282.json, 视频生成/图生视频/1981180403119808514.json, 视频生成/文生视频/1961428825634750466.json, 视频生成/文生视频/1970462683160080385.json, 视频生成/文生视频/Supermate 推荐Qwen3vl视频反推提示+Video_wan2_2_14B视频生成_1982073877964693505.json, 视频生成/文生视频/wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_199

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1953391990853521409.json、图片生成/文生图/1961428825634750466.json、图片生成/文生图/1970462683160080385.json、图片生成/文生图/1989283451264225282.json、视频生成/图生视频/1981180403119808514.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `JWStringMultiline` —— 6/9 个有
- `JoinStringMulti` —— 6/9 个有
- `String` —— 6/9 个有
- `PreviewImage` —— 4/9 个有
- `AILab_QwenVL` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 9 | 100% |
| 采样算法 | 2.5 | 1 - 2.5 | 9 | 65% |
| 调度器 | ddim | - | 9 | 67% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2.5，观测区间 1 - 2.5，9 个样本
- 调度器 最常用 ddim，9 个样本，一致性 67%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
