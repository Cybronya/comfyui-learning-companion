---
name: unknown_workflow_video_sampler_vae_28
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.92275
common_nodes: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, RH_Translator, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Ditto图片风格转绘_1981268088685584385.json, 平台全量/Ditto视频转绘为真实风格_1982419885370286081.json, 平台全量/Ditto视频转绘为真实风格_2084254233427271681.json, 平台全量/Ditto视频风格转绘_1980452276194226177.json, 平台全量/Ditto视频风格转绘_1995865138488041473.json, 平台全量/Ditto视频风格转绘_2059087975048368130.json, 平台全量/Ditto视频风格转绘_2072893396791943169.json, 平台全量/视频风格转绘_1980873904069722113.json, 平台全量/视频风格转绘_2012052305805320194.json, 平台全量/视频风格转绘_2045026049209143297.json, 平台全量/视频风格转绘_2046385739801305090.json, 视频生成/图生视频/ditto视频风格转绘工作流_1980897835057106945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_28

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Ditto图片风格转绘_1981268088685584385.json、平台全量/Ditto视频转绘为真实风格_1982419885370286081.json、平台全量/Ditto视频转绘为真实风格_2084254233427271681.json、平台全量/Ditto视频风格转绘_1980452276194226177.json、平台全量/Ditto视频风格转绘_1995865138488041473.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Translator`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 11/12 个有
- `LoadWanVideoT5TextEncoder` —— 11/12 个有
- `ShowText|pysssss` —— 11/12 个有
- `String` —— 11/12 个有
- `VHS_LoadVideo` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `VHS_VideoInfoLoaded` —— 11/12 个有
- `WanVideoBlockSwap` —— 11/12 个有
- `WanVideoLoraSelect` —— 11/12 个有
- `WanVideoVACEModelSelect` —— 11/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `LoadImage` —— 6/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `Int` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
