---
name: unknown_workflow_sampler_clip_unet_209
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.910833
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_wan2_2_5B_ti2v.json, comfyui-workflow-templates-json/video_wan_ati.json, comfyui-workflow-templates-json/wan2.1_flf2v_720_f16.json, 图片生成/图生图/WanFLF2V + CausVid lora速度提升首尾帧视频_1936806458011062274.json, 视频生成/图生视频/03-04-01-WAN2.1-首尾帧生成视频-FLF2V-原生_1989234682468372481.json, 视频生成/图生视频/Wan2.1 FL2fV 首尾帧_1948615618990866434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_209

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2_2_5B_ti2v.json、comfyui-workflow-templates-json/video_wan_ati.json、comfyui-workflow-templates-json/wan2.1_flf2v_720_f16.json、图片生成/图生图/WanFLF2V + CausVid lora速度提升首尾帧视频_1936806458011062274.json、视频生成/图生视频/03-04-01-WAN2.1-首尾帧生成视频-FLF2V-原生_1989234682468372481.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 5/6 个有
- `CLIPVisionLoader` —— 5/6 个有
- `WanFirstLastFrameToVideo` —— 4/6 个有
- `CreateVideo` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `LoadImageFromUrl` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `Wan22ImageToVideoLatent` —— 1/6 个有
- `WanTrackToVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 6 | 75% |
| Prompt 约束强度(CFG) | 3 | 1 - 5 | 6 | 62% |
| 采样算法 | uni_pc | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 5，6 个样本
- 采样算法 最常用 uni_pc，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
