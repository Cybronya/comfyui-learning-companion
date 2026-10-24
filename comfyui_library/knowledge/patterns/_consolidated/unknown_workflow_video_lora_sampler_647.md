---
name: unknown_workflow_video_lora_sampler_647
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.954667
common_nodes: [CLIPLoader, CLIPTextEncode, DWPreprocessor, DepthAnythingV2Preprocessor, ImageBlend, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/WanVace快速视频动作迁移_1934797316740325377.json, 视频生成/图生视频/wan2.1 vace 动作参考视频生成_1933802082413797378.json, 视频生成/图生视频/首帧视频转绘（AI匹夫）_1956996435298410498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_647

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/WanVace快速视频动作迁移_1934797316740325377.json、视频生成/图生视频/wan2.1 vace 动作参考视频生成_1933802082413797378.json、视频生成/图生视频/首帧视频转绘（AI匹夫）_1956996435298410498.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `ImageBlend`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/3 个有
- `ChinesePrompt_Mix` —— 1/3 个有
- `ImageCrop` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 7 - 8 | 3 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | ddim | - | 3 | 100% |
| 调度器 | ddim_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 7 - 8，3 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 ddim，3 个样本，一致性 100%
- 调度器 最常用 ddim_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
