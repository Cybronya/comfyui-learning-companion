---
name: unknown_workflow_lora_sampler_unet_80
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.86825
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_万物转水墨动漫风格_2052662192381669377.json, 图片生成/图生图/Qwen_转-通透动漫风格_2051951433578233857.json, 图片生成/图生图/Qwen_转Anmi质感通透动漫风格_2052224157546491906.json, 图片生成/图生图/printing_extraction_api_2100774516120186882.json, 图片生成/图生图/万物皆可Q：IP角色一键智绘Q版风格_2056237735295410178.json, 图片生成/图生图/人物图像生成动漫Q版动画人物IP角色一键智绘Q版风格_2077294254203949058.json, 图片生成/图生图/印花提取——qwen2511_2096790576627802114.json, 图片生成/图生图/印花提取——qwen2511_2097136560390103041.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_80

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen_万物转水墨动漫风格_2052662192381669377.json、图片生成/图生图/Qwen_转-通透动漫风格_2051951433578233857.json、图片生成/图生图/Qwen_转Anmi质感通透动漫风格_2052224157546491906.json、图片生成/图生图/printing_extraction_api_2100774516120186882.json、图片生成/图生图/万物皆可Q：IP角色一键智绘Q版风格_2056237735295410178.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Easy_QwenEdit2509` —— 5/8 个有
- `CLIPTextEncode` —— 3/8 个有
- `CropWithPadInfo_EditUtils` —— 3/8 个有
- `QwenEditConfigPreparer` —— 3/8 个有
- `QwenEditOutputExtractor_EditUtils` —— 3/8 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `ImageScale` —— 1/8 个有
- `TT_img_enc` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
