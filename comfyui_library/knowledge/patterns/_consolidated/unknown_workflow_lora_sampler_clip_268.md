---
name: unknown_workflow_lora_sampler_clip_268
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.976333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PixelPerfectResolution, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/wan2.2动作迁移_2040787397574664194.json, 视频生成/图生视频/▶Wan2.2-Animate动作迁移流原创作者-黑鹤001_2042244068767436801.json, 视频生成/图生视频/低显存GGUF-Wan2.2-Animate动作迁移流_2030541873395273730.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_268

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/wan2.2动作迁移_2040787397574664194.json、视频生成/图生视频/▶Wan2.2-Animate动作迁移流原创作者-黑鹤001_2042244068767436801.json、视频生成/图生视频/低显存GGUF-Wan2.2-Animate动作迁移流_2030541873395273730.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
