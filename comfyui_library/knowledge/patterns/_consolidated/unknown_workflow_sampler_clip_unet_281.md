---
name: unknown_workflow_sampler_clip_unet_281
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8642
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2 文生图_1954733353410949121.json, 图片生成/文生图/Wan2.2文生图工作流——comfyui官方版_1951146831617175554.json, 图片生成/文生图/[🛫书墨]wan2_2lightning加速lora__10秒_1952444989798330370.json, 图片生成/文生图/wan2.1单帧文生图_1944002361066946562.json, 图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_281

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Wan2.2 文生图_1954733353410949121.json、图片生成/文生图/Wan2.2文生图工作流——comfyui官方版_1951146831617175554.json、图片生成/文生图/[🛫书墨]wan2_2lightning加速lora__10秒_1952444989798330370.json、图片生成/文生图/wan2.1单帧文生图_1944002361066946562.json、图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `LoraLoader` —— 2/5 个有
- `WanVideoNAG` —— 2/5 个有
- `CFGZeroStarAndInit` —— 1/5 个有
- `FastFilmGrain` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |
| 采样步数 | 10 | 5 - 10 | 5 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 5 | 33% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样步数 中位数 10，观测区间 5 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
