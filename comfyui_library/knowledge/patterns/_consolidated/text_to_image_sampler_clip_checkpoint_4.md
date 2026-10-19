---
name: text_to_image_sampler_clip_checkpoint_4
type: Text To Image
frequency: 11
level: moderate
coverage: 0.748909
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_sdxl_simple.json, comfyui-workflow-templates-json/sdxl_revision_text_prompts.json, sd1.5/basic.json, 图片生成/文生图/1951180182470242305.json, 图片生成/文生图/1958497485645836289.json, 图片生成/文生图/1961283334359990274.json, 图片生成/文生图/1962370527010623489.json, 图片生成/文生图/1979111789180915714.json, 图片生成/文生图/1979377865538048002.json, 图片生成/文生图/1979390293403406337.json, 图片生成/文生图/1979445307241041922.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（comfyui-workflow-templates-json/image_sdxl_simple.json、comfyui-workflow-templates-json/sdxl_revision_text_prompts.json、sd1.5/basic.json、图片生成/文生图/1951180182470242305.json、图片生成/文生图/1958497485645836289.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/11 个有
- `CLIPVisionEncode` —— 1/11 个有
- `CLIPVisionLoader` —— 1/11 个有
- `unCLIPConditioning` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 35 | 11 | 67% |
| Prompt 约束强度(CFG) | 7 | 1.5 - 8 | 11 | 66% |
| 采样算法 | dpmpp_2m_sde | - | 11 | 36% |
| 调度器 | karras | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 768 | 512 - 1024 | 11 | 73% |
| 高度 | 768 | 512 - 1216 | 11 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 35，11 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 1.5 - 8，11 个样本
- 采样算法 最常用 dpmpp_2m_sde，11 个样本，一致性 36%
- 调度器 最常用 karras，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1024，11 个样本
- 高度 中位数 768，观测区间 512 - 1216，11 个样本
