---
name: unknown_workflow_sampler_clip_unet_75
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.878846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json, 图片生成/反推提示词/4bjs_2052395586623684609.json, 图片生成/反推提示词/50pptmake_2051255545180499970.json, 图片生成/反推提示词/72wstzs_2052609391525933058.json, 图片生成/反推提示词/79manhuawst_2053041688037347330.json, 图片生成/图生图/Z 文生图（厨房模型）_2000808844013993985.json, 图片生成/文生图/Qwen2512文生图工作流_2026224981025234945.json, 图片生成/文生图/Z 手持质感 文生图_2021145496873607169.json, 图片生成/文生图/Z-Image-Turbo LoRA 出图+放大_2018944118063370242.json, 图片生成/文生图/Z_image_高清放大_2002351849619505154.json, 图片生成/文生图/Z_image告别图片单一性（蓝色多脑盒）_2000908501360799745.json, 图片生成/文生图/lora生图_2_2019229829660418050.json, 图片生成/文生图/女团生成器_Zimage_2003080375004012545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json、图片生成/反推提示词/4bjs_2052395586623684609.json、图片生成/反推提示词/50pptmake_2051255545180499970.json、图片生成/反推提示词/72wstzs_2052609391525933058.json、图片生成/反推提示词/79manhuawst_2053041688037347330.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 11/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `SeedVR2` —— 7/13 个有
- `SeedVR2BlockSwap` —— 7/13 个有
- `Fast Groups Bypasser (rgthree)` —— 6/13 个有
- `ConditioningZeroOut` —— 5/13 个有
- `Image Comparer (rgthree)` —— 5/13 个有
- `SeedVR2ExtraArgs` —— 5/13 个有
- `RTXVideoSuperResolution` —— 4/13 个有
- `easy cleanGpuUsed` —— 4/13 个有
- `DuckHideNode` —— 1/13 个有
- `LoraLoader` —— 1/13 个有
- `MultiLinePromptIndex` —— 1/13 个有
- `StringConcatenate` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 1 - 10 | 13 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 13 | 65% |
| 采样算法 | euler | - | 13 | 62% |
| 调度器 | simple | - | 13 | 77% |
| 重绘幅度 | 1 | 0.8 - 1 | 13 | 95% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 1 - 10，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 62%
- 调度器 最常用 simple，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，13 个样本，取值集中（一致性 95%）
- 高发问题（12/13 个样本）：Steps较低可能导致细节不足
