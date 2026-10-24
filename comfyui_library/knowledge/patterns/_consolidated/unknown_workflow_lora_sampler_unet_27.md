---
name: unknown_workflow_lora_sampler_unet_27
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.978133
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI短剧角色换装换动作 Qwen-image-edit2511+SeedVR2高清多图参考图生图_2018199405492441089.json, 图片生成/图生图/FireRed-Image-Edit 换装神器｜电商服装展示_2104411613049741314.json, 图片生成/图生图/Qwen Edit Plus 多图编辑_1970549322146344962.json, 图片生成/图生图/rick and morty_2002342394169311234.json, 图片生成/图生图/五图编辑-rh-Qwen-Edit-2511-模板_2014144550574493697.json, 图片生成/图生图/动漫短剧角色换装换动作 Qwen-image-edit2511多图参考图生图_2015042670699220994.json, 图片生成/图生图/单图编辑-rh-Qwen-Edit-2511-模板_2013616947384029186.json, 图片生成/图生图/去水印-Qwen-Edit-2511 图片去水印_2036840450740457474.json, 图片生成/图生图/去水印-图片去水印-Qwen-Edit-2511-图像编辑_2025387125960613889.json, 图片生成/图生图/去水印-图片去水印-Qwen-Edit-2511-图像编辑_2026918010535026689.json, 图片生成/图生图/叁图编辑-rh-Qwen-Edit-2511-模板_2013999350959054850.json, 图片生成/图生图/双图编辑-Qwen-Edit-2511-模板_2013899588947681282.json, 图片生成/图生图/四图编辑-rh-Qwen-Edit-2511-模板_2014144556878536705.json, 图片生成/图生图/图片去水印极速版-阿浩_2031530848842944514.json, 图片生成/图生图/老照片修复-Qwen-Edit-2511-图像编辑_2003754424059240449.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_27

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/AI短剧角色换装换动作 Qwen-image-edit2511+SeedVR2高清多图参考图生图_2018199405492441089.json、图片生成/图生图/FireRed-Image-Edit 换装神器｜电商服装展示_2104411613049741314.json、图片生成/图生图/Qwen Edit Plus 多图编辑_1970549322146344962.json、图片生成/图生图/rick and morty_2002342394169311234.json、图片生成/图生图/五图编辑-rh-Qwen-Edit-2511-模板_2014144550574493697.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 12/15 个有
- `EmptySD3LatentImage` —— 10/15 个有
- `Int` —— 7/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/15 个有
- `SmartImageConcat` —— 4/15 个有
- `LayerUtility: PurgeVRAM V2` —— 2/15 个有
- `PrimitiveStringMultiline` —— 2/15 个有
- `Image Comparer (rgthree)` —— 1/15 个有
- `JjkText` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `SeedVR2GGUF` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 15 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | sa_solver | - | 15 | 67% |
| 调度器 | simple | - | 15 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，15 个样本，一致性 67%
- 调度器 最常用 simple，15 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（14/15 个样本）：Steps较低可能导致细节不足
