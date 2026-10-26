---
name: unknown_workflow_lora_sampler_unet_70
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.709333
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Get Image Size, GrowMaskWithBlur, GulfSeaImageMergeMask, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveInt, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader, 图像缩放V2_孤海, 孤海外补画板按方向]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511 最强无损扩图流｜零偏移｜零色差｜零接缝_2077741666592706561.json, 图片生成/图生图/”构图太窄？？”“裁剪过度？？”试了100多种扩图方法，终于做出中间一点不变的最炸无损封神扩图流！！_2065800262656286722.json, 图片生成/图生图/史上最强_扩图__2097159314808066050.json, 图片生成/图生图/史上最强_扩图__2097499447767953410.json, 图片生成/图生图/无损封神一键扩图工作流！！_2095769504977612801.json, 图片生成/图生图/无损封神一键扩图工作流！！_2096062738471673857.json, 图片生成/图生图/最强  _扩图_生成器_2078405944349913090.json, 图片生成/图生图/零接缝零色差零偏移最强无损扩图流2511Qwen_2085192513094246402.json, 图片生成/图生图/零接缝零色差零偏移最强无损扩图流2511Qwen_2085207727323832321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_70

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen 2511 最强无损扩图流｜零偏移｜零色差｜零接缝_2077741666592706561.json、图片生成/图生图/”构图太窄？？”“裁剪过度？？”试了100多种扩图方法，终于做出中间一点不变的最炸无损封神扩图流！！_2065800262656286722.json、图片生成/图生图/史上最强_扩图__2097159314808066050.json、图片生成/图生图/史上最强_扩图__2097499447767953410.json、图片生成/图生图/无损封神一键扩图工作流！！_2095769504977612801.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Get Image Size`
- `GrowMaskWithBlur`
- `GulfSeaImageMergeMask`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `图像缩放V2_孤海`
- `孤海外补画板按方向`

**可变部分**（部分 workflow 才有）：
- `DF_Text_Box` —— 6/9 个有
- `GetNode` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `RHHiddenNodes` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `Text Concatenate` —— 3/9 个有
- `easy int` —— 3/9 个有
- `孤海注释` —— 3/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler_ancestral | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
