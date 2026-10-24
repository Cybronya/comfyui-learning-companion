---
name: text_to_image_lora_sampler_clip_118
type: Text To Image
frequency: 12
level: strong
coverage: 0.885083
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, CR Text Replace, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ProcessString, SaveImage, Seed (rgthree), Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image主体一致性反推生分镜_2008852899228557314.json, 图片生成/图生图/快速洗图版v22_1999381371757920257.json, 图片生成/图生图/（大网渔网袜量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1995173381853130754.json, 图片生成/图生图/（小情绪量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1999760613897367553.json, 图片生成/图生图/（贞贞-量贩版）Z-Image-Turbo D-OPSD美少女文生图V1_2056788439630176258.json, 图片生成/图生图/🏇超快速美女孵蛋器超然洗图版V1🏇_1995386236758110209.json, 图片生成/文生图/Red Z-Image Vs Z-image Turbo对比_1998113383687839745.json, 图片生成/文生图/Z-Image-Turbo  D-OPSD美少女文生图_2058718122760302593.json, 图片生成/文生图/Z-Image-Turbo D-OPSD美少女文生图V1_2058219333456842754.json, 图片生成/文生图/Z-image 超快速美女孵蛋器超然升级版V1_1995339133893718018.json, 图片生成/文生图/🏇超快速美女孵蛋器超然升级版V1🏇_1995296859344318466.json, 图片生成/文生图/🏇超快速美女孵蛋器超然升级版【本地版】🏇_1995302605654044674.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Z-image主体一致性反推生分镜_2008852899228557314.json、图片生成/图生图/快速洗图版v22_1999381371757920257.json、图片生成/图生图/（大网渔网袜量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1995173381853130754.json、图片生成/图生图/（小情绪量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1999760613897367553.json、图片生成/图生图/（贞贞-量贩版）Z-Image-Turbo D-OPSD美少女文生图V1_2056788439630176258.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CR Text Replace`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_Pro_Node` —— 10/12 个有
- `easy showAnything` —— 7/12 个有
- `ImpactInt` —— 6/12 个有
- `LoadImage` —— 4/12 个有
- `Note Plus (mtb)` —— 4/12 个有
- `easy anythingIndexSwitch` —— 3/12 个有
- `Qwen3VL_Chat` —— 2/12 个有
- `AddLabel` —— 1/12 个有
- `CheckpointLoaderSimple` —— 1/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `图像缩放V2_孤海` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 12 | 100% |
| 高度 | 1920 | 1920 - 1920 | 12 | 100% |
| 采样步数 | 10 | 10 - 10 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler_ancestral | - | 12 | 50% |
| 调度器 | sgm_uniform | - | 12 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，12 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
