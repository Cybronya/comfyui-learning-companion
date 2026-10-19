---
name: text_to_image_sampler_clip_checkpoint_13
type: Text To Image
frequency: 3
level: moderate
coverage: 0.914333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageOnlyCheckpointLoader, KSampler, PreviewImage, SVD_img2vid_Conditioning, VAEDecode, VideoLinearCFGGuidance]
problems: []
missing: []
members: [comfyui-workflow-templates-json/txt_to_image_to_video.json, 视频生成/文生视频/1845741279811661826.json, 视频生成/文生视频/1801584137573183489.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/txt_to_image_to_video.json、视频生成/文生视频/1845741279811661826.json、视频生成/文生视频/1801584137573183489.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageOnlyCheckpointLoader`
- `KSampler`
- `PreviewImage`
- `SVD_img2vid_Conditioning`
- `VAEDecode`
- `VideoLinearCFGGuidance`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 15 - 50 | 3 | 45% |
| Prompt 约束强度(CFG) | 7 | 2.5 - 8 | 3 | 59% |
| 采样算法 | uni_pc_bh2 | - | 3 | 33% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 960 - 1280 | 3 | 87% |
| 高度 | 768 | 576 - 1536 | 3 | 57% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 15 - 50，3 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 7，观测区间 2.5 - 8，3 个样本
- 采样算法 最常用 uni_pc_bh2，3 个样本，一致性 33%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 960 - 1280，3 个样本，取值集中（一致性 87%）
- 高度 中位数 768，观测区间 576 - 1536，3 个样本
