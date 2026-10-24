---
name: unknown_workflow_sampler_clip_unet_398
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.914667
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/膨胀沙发变化_2034620365376331777.json, 视频生成/图生视频/🔥Fun模型首测！让3D卡通人物跳起来！(基于wan2.2升级，含ComfyUI工作流)_1956204129557336066.json, 视频生成/文生视频/【阡陌】 Wan2.2 Fun Control 视频控制生成_1969656393957601281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_398

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/膨胀沙发变化_2034620365376331777.json、视频生成/图生视频/🔥Fun模型首测！让3D卡通人物跳起来！(基于wan2.2升级，含ComfyUI工作流)_1956204129557336066.json、视频生成/文生视频/【阡陌】 Wan2.2 Fun Control 视频控制生成_1969656393957601281.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `Wan22FunControlToVideo` —— 2/3 个有
- `WanFirstLastFrameToVideo` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `WanFunInpaintToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 3 | 19% |
| 采样算法 | 1 | 1 - 4 | 3 | 29% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，3 个样本，取值分散，一致性仅 19%
- 采样算法 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
