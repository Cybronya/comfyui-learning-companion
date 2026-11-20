---
name: unknown_workflow_lora_sampler_unet_88
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.904222
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2509多图参考API专用_1999488679565553665.json, 图片生成/图生图/QwenEdit——2511_2004160555151728641.json, 图片生成/图生图/Qwen_万物转水墨动漫风格_2052662192381669377.json, 图片生成/图生图/Qwen_转-通透动漫风格_2051951433578233857.json, 图片生成/图生图/Qwen_转Anmi质感通透动漫风格_2052224157546491906.json, 图片生成/图生图/真人转动漫风格_2058356461167800322.json, 图片生成/图生图/真人转动漫风格_2090648180265414657.json, 图片生成/文生图/2511 多角度_2019257618123984898.json, 平台全量/电商定制 打印到产品_2057468622737592321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_88

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen2509多图参考API专用_1999488679565553665.json、图片生成/图生图/QwenEdit——2511_2004160555151728641.json、图片生成/图生图/Qwen_万物转水墨动漫风格_2052662192381669377.json、图片生成/图生图/Qwen_转-通透动漫风格_2051951433578233857.json、图片生成/图生图/Qwen_转Anmi质感通透动漫风格_2052224157546491906.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `Easy_QwenEdit2509` —— 6/9 个有
- `EmptySD3LatentImage` —— 3/9 个有
- `TextEncodeQwenImageEditPlus` —— 3/9 个有
- `TextEncodeQwenImageEdit` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `ImpactImageInfo` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `easy int` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
