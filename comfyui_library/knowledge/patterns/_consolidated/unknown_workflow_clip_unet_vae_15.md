---
name: unknown_workflow_clip_unet_vae_15
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.815667
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, CreateVideo, GetVideoComponents, LoadImage, LoadVideo, ModelSamplingSD3, PreviewImage, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_wan2_2_14B_fun_control.json, comfyui-workflow-templates-json/video_wan2_2_5B_fun_control.json, comfyui-workflow-templates-json/video_wan_vace_14B_v2v.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_15

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2_2_14B_fun_control.json、comfyui-workflow-templates-json/video_wan2_2_5B_fun_control.json、comfyui-workflow-templates-json/video_wan_vace_14B_v2v.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `CreateVideo`
- `GetVideoComponents`
- `LoadImage`
- `LoadVideo`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 2/3 个有
- `Wan22FunControlToVideo` —— 2/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `SaveAnimatedWEBP` —— 1/3 个有
- `TrimVideoLatent` —— 1/3 个有
- `WanVaceToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 5 | 1 - 20 | 3 | 6% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.3 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 20，3 个样本，取值分散，一致性仅 6%
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
