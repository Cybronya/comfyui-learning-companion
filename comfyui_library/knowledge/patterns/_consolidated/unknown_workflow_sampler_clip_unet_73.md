---
name: unknown_workflow_sampler_clip_unet_73
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.889917
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json, 图片生成/反推提示词/4bjs_2052395586623684609.json, 图片生成/反推提示词/50pptmake_2051255545180499970.json, 图片生成/反推提示词/72wstzs_2052609391525933058.json, 图片生成/反推提示词/79manhuawst_2053041688037347330.json, 图片生成/图生图/Z 文生图（厨房模型）_2000808844013993985.json, 图片生成/文生图/Qwen2512文生图工作流_2026224981025234945.json, 图片生成/文生图/Y-Z-Image-turbo+lenovo lora-workflow_1995640202892861441.json, 图片生成/文生图/Y-Z-Image-turbo+zit-flow-dpo-lora-workflow_2029147456390303745.json, 图片生成/文生图/Z 手持质感 文生图_2021145496873607169.json, 图片生成/文生图/Z_image告别图片单一性（蓝色多脑盒）_2000908501360799745.json, 图片生成/文生图/女团生成器_Zimage_2003080375004012545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json、图片生成/反推提示词/4bjs_2052395586623684609.json、图片生成/反推提示词/50pptmake_2051255545180499970.json、图片生成/反推提示词/72wstzs_2052609391525933058.json、图片生成/反推提示词/79manhuawst_2053041688037347330.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 10/12 个有
- `LoraLoaderModelOnly` —— 8/12 个有
- `easy cleanGpuUsed` —— 6/12 个有
- `ConditioningZeroOut` —— 5/12 个有
- `Fast Groups Bypasser (rgthree)` —— 5/12 个有
- `RTXVideoSuperResolution` —— 4/12 个有
- `SeedVR2` —— 4/12 个有
- `SeedVR2BlockSwap` —— 4/12 个有
- `SeedVR2ExtraArgs` —— 4/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `SDXLAspectRatio` —— 2/12 个有
- `DuckHideNode` —— 1/12 个有
- `LoraLoader` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 1 - 10 | 12 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 64% |
| 采样算法 | euler | - | 12 | 58% |
| 调度器 | simple | - | 12 | 75% |
| 重绘幅度 | 1 | 0.8 - 1 | 12 | 94% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 1 - 10，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 58%
- 调度器 最常用 simple，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，12 个样本，取值集中（一致性 94%）
- 高发问题（11/12 个样本）：Steps较低可能导致细节不足
