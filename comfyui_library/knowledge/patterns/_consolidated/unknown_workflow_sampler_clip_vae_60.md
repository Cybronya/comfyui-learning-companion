---
name: unknown_workflow_sampler_clip_vae_60
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.97375
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, SaveVideo, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-Lightx2v latest_1988041568177295362.json, 视频生成/图生视频/Wan2.2-Lightx2v-1108新版加速LoRA_1988138088604004353.json, 视频生成/图生视频/Wan2.2_14B_图生视频-加速版-KJ模型_1950521447607357441.json, 视频生成/图生视频/wan2.2_14B_VACE_GGUF_图生视频-加速版_1950557926740119553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-Lightx2v latest_1988041568177295362.json、视频生成/图生视频/Wan2.2-Lightx2v-1108新版加速LoRA_1988138088604004353.json、视频生成/图生视频/Wan2.2_14B_图生视频-加速版-KJ模型_1950521447607357441.json、视频生成/图生视频/wan2.2_14B_VACE_GGUF_图生视频-加速版_1950557926740119553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelSamplingSD3` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `WanImageToVideo` —— 3/4 个有
- `ImpactInt` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `Text` —— 2/4 个有
- `TrimVideoLatent` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `WanVaceToVideo` —— 1/4 个有
- `workflow>LORA1` —— 1/4 个有
- `workflow>LORA2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 20 | 4 | 47% |
| 采样算法 | 1 | 1 - 3.5 | 4 | 33% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 20，4 个样本，取值分散，一致性仅 47%
- 采样算法 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
