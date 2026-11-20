---
name: unknown_workflow_lora_sampler_unet_26
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.943222
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_肤质优化_2072888068935340033.json, 图片生成/图生图/seedance2.0真人过审核方法（适用于豆包、即梦、小云雀）_2037113635297828866.json, 图片生成/图生图/seedance2.0真人过审脸部拆解（适用于即梦）fast_2037525850534453249.json, 图片生成/图生图/一键换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2101599676305854466.json, 图片生成/图生图/一键换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2110816443343396866.json, 图片生成/图生图/三视图-Qwen2511-高度一致性_2071975841445269506.json, 图片生成/图生图/三视图-三视图一键生成-Qwen-Edit-2511-保持高度一致性_2023398149548675073.json, 图片生成/图生图/即梦、小云雀、豆包、seedance2.0真人过审核方法-Qwen-2511_2036336291356352513.json, 图片生成/图生图/即梦、小云雀、豆包、超能视频2.0真人过审核方法-Qwen-2511_2034590390044598273.json, 图片生成/图生图/双图服装试 穿电商换装_2100599874197737474.json, 图片生成/图生图/小红书  FireRed-Image-Edit   换装 换衣  电商服装展示_2093008142111166466.json, 图片生成/图生图/换装+换衣 Outfit Changes  Clothing Changes FireRed_2102936109482336257.json, 图片生成/图生图/换装商用级 高度一致性 高清_2104130241412292610.json, 图片生成/图生图/换装简洁版 换衣简洁版   电商服装展示 FireRed-Image-Edit 小红书_2079795242282340354.json, 图片生成/图生图/电商换装丨双图服装试穿_2100138204581163009.json, 图片生成/图生图/电商换装丨双图服装试穿_2101857775021281282.json, 图片生成/图生图/电商换装丨双图服装试穿_2102673132061552641.json, 图片生成/图生图/电商服装展示_换装 换衣_2078741577014534146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/qwen_肤质优化_2072888068935340033.json、图片生成/图生图/seedance2.0真人过审核方法（适用于豆包、即梦、小云雀）_2037113635297828866.json、图片生成/图生图/seedance2.0真人过审脸部拆解（适用于即梦）fast_2037525850534453249.json、图片生成/图生图/一键换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2101599676305854466.json、图片生成/图生图/一键换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2110816443343396866.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 18 个 workflow 都包含：
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
- `PreviewImage` —— 12/18 个有
- `PIP_图像联结` —— 11/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/18 个有
- `EmptySD3LatentImage` —— 6/18 个有
- `CustomAddLabel` —— 5/18 个有
- `Image Comparer (rgthree)` —— 1/18 个有
- `SeedVR2` —— 1/18 个有
- `SeedVR2BlockSwap` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 18 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 67% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 67%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（22/18 个样本）：Steps较低可能导致细节不足
