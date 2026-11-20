---
name: unknown_workflow_lora_sampler_unet_46
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.970182
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI短剧角色换装换动作 Qwen-image-edit2511+SeedVR2高清多图参考图生图_2018199405492441089.json, 图片生成/图生图/FireRed-Image-Edit 换装神器｜电商服装展示_2104411613049741314.json, 图片生成/图生图/Qwen Edit Plus 多图编辑_1970549322146344962.json, 图片生成/图生图/rick and morty_2002342394169311234.json, 图片生成/图生图/动漫短剧角色换装换动作 Qwen-image-edit2511多图参考图生图_2015042670699220994.json, 图片生成/图生图/去水印-Qwen-Edit-2511 图片去水印_2036840450740457474.json, 图片生成/图生图/去水印-图片去水印-Qwen-Edit-2511-图像编辑_2025387125960613889.json, 图片生成/图生图/去水印-图片去水印-Qwen-Edit-2511-图像编辑_2026918010535026689.json, 图片生成/图生图/图片去水印极速版-阿浩_2031530848842944514.json, 图片生成/图生图/老照片修复-Qwen-Edit-2511-图像编辑_2003754424059240449.json, 图片生成/文生图/Qwen-Edit-2511-三图融合-一致性加强版本_2026276649716682754.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_46

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/AI短剧角色换装换动作 Qwen-image-edit2511+SeedVR2高清多图参考图生图_2018199405492441089.json、图片生成/图生图/FireRed-Image-Edit 换装神器｜电商服装展示_2104411613049741314.json、图片生成/图生图/Qwen Edit Plus 多图编辑_1970549322146344962.json、图片生成/图生图/rick and morty_2002342394169311234.json、图片生成/图生图/动漫短剧角色换装换动作 Qwen-image-edit2511多图参考图生图_2015042670699220994.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
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
- `CR Text` —— 8/11 个有
- `Int` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/11 个有
- `EmptySD3LatentImage` —— 6/11 个有
- `LayerUtility: PurgeVRAM V2` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `SeedVR2GGUF` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 11 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | sa_solver | - | 11 | 55% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，11 个样本，一致性 55%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
