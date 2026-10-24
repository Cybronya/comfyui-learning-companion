---
name: unknown_workflow_video_sampler_clip_193
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.915333
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), INTConstant, ImageResizeKJv2, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan22-Remix图生视频_2042575969071931394.json, 视频生成/图生视频/▶Wan22-Remix-视频流(整合)_2030903801942642689.json, 视频生成/图生视频/空白工作流_2043827022673219585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_193

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan22-Remix图生视频_2042575969071931394.json、视频生成/图生视频/▶Wan22-Remix-视频流(整合)_2030903801942642689.json、视频生成/图生视频/空白工作流_2043827022673219585.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `WanFirstLastFrameToVideo` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `FloatConstant` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
