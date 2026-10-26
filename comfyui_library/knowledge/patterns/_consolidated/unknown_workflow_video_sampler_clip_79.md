---
name: unknown_workflow_video_sampler_clip_79
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.967125
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/WAN2.2 泼水换装 画风真实 运行流畅 可更换lora_1953283354574712834.json, 视频生成/图生视频/Wan2.2 整合模型超快图生视频_1950706525243396097.json, 视频生成/图生视频/Wan_FusionX_i2v_Native-Y-Workflow_1934825065211207682.json, 视频生成/图生视频/comfyUI 官方wan2.1 lora特效工作流_1899683017957265409.json, 视频生成/图生视频/wan2.1_GGUF官方工作流_I2V_480P_1930296715969204225.json, 视频生成/图生视频/wan2.1_lora_官方工作流_gguf版_480P_1930311373908250626.json, 视频生成/图生视频/wan2.1挤压效果_1898936758191771650.json, 视频生成/图生视频/喝西北风_1911197940504035330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_79

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/WAN2.2 泼水换装 画风真实 运行流畅 可更换lora_1953283354574712834.json、视频生成/图生视频/Wan2.2 整合模型超快图生视频_1950706525243396097.json、视频生成/图生视频/Wan_FusionX_i2v_Native-Y-Workflow_1934825065211207682.json、视频生成/图生视频/comfyUI 官方wan2.1 lora特效工作流_1899683017957265409.json、视频生成/图生视频/wan2.1_GGUF官方工作流_I2V_480P_1930296715969204225.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 7/8 个有
- `CLIPVisionEncode` —— 6/8 个有
- `CLIPVisionLoader` —— 6/8 个有
- `UNETLoader` —— 5/8 个有
- `UnetLoaderGGUF` —— 4/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `EmptyHunyuanLatentVideo` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `SaveAnimatedWEBP` —— 2/8 个有
- `WanVideoTeaCacheKJ` —— 2/8 个有
- `ApplySageAttention` —— 1/8 个有
- `TeaCache` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 4 - 30 | 8 | 42% |
| Prompt 约束强度(CFG) | 5.985 | 1 - 6 | 8 | 41% |
| 采样算法 | uni_pc | - | 8 | 75% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 0.65 | - | 2 | 46% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 4 - 30，8 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 5.985，观测区间 1 - 6，8 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 uni_pc，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
