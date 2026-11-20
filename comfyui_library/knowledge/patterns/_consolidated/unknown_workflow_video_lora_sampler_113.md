---
name: unknown_workflow_video_lora_sampler_113
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.778667
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ComfyMathExpression, ContextWindowsManual, GetImageRangeFromBatch, ImageFromBatch, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SamplerCustom, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimate2Cache, WanAnimate2ToVideo]
problems: []
missing: []
members: [数字人/数字人/Animate2动作迁移循环流_2087178729373130754.json, 数字人/数字人/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2106306747928498177.json, 数字人/数字人/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2106379041409421313.json, 数字人/数字人/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2114691557663264769.json, 视频生成/图生视频/Animate2-动作迁移（长视频for循环）_2087535506614743041.json, 视频生成/图生视频/Animate2-数字人唱歌_跳舞-动作迁移-不限时长-循环流_2086985804689268738.json, 视频生成/图生视频/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移15秒内_2087549782628847618.json, 视频生成/图生视频/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2097276416403533826.json, 视频生成/图生视频/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2097297241835921409.json, 视频生成/图生视频/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2114671698929872898.json, 视频生成/图生视频/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移无限时长V1_2086760732246499329.json, 视频生成/图生视频/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移无限时长加速版_2087045861942579202.json, 视频生成/图生视频/wan-animate2动作姿势模仿_2087054631615680514.json, 视频生成/文生视频/Animate2动作迁移_2104741113713217538.json, 视频生成/文生视频/Wan animate2 视频编辑 循环流V1_2086206809366421506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（数字人/数字人/Animate2动作迁移循环流_2087178729373130754.json、数字人/数字人/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2106306747928498177.json、数字人/数字人/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2106379041409421313.json、数字人/数字人/Animate2数字人_跳舞_视频编辑_唱歌_动作迁移_复刻动作无限时长_2114691557663264769.json、视频生成/图生视频/Animate2-动作迁移（长视频for循环）_2087535506614743041.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ComfyMathExpression`
- `ContextWindowsManual`
- `GetImageRangeFromBatch`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimate2Cache`
- `WanAnimate2ToVideo`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 14/15 个有
- `ImageResizeKJv2` —— 14/15 个有
- `ResizeImageMaskNode` —— 14/15 个有
- `VHS_VideoInfo` —— 14/15 个有
- `easy int` —— 14/15 个有
- `GetImageSize` —— 13/15 个有
- `PrimitiveStringMultiline` —— 13/15 个有
- `TensorLoopClose` —— 13/15 个有
- `TensorLoopOpen` —— 13/15 个有
- `ComfySwitchNode` —— 12/15 个有
- `GetNode` —— 12/15 个有
- `JWInteger` —— 12/15 个有
- `ImageConcatMulti` —— 11/15 个有
- `PrimitiveBoolean` —— 11/15 个有
- `easy showAnything` —— 10/15 个有
- `SetNode` —— 3/15 个有
- `easy forLoopEnd` —— 2/15 个有
- `easy forLoopStart` —— 2/15 个有
- `Bookmark (rgthree)` —— 1/15 个有
- `DF_Int_to_Float` —— 1/15 个有
- `Int` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `MathExpression|pysssss` —— 1/15 个有
- `Note Plus (mtb)` —— 1/15 个有
- `PlaySound|pysssss` —— 1/15 个有
- `ShowAnything|Mie` —— 1/15 个有
- `SimpleMath+` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
