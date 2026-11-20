---
name: unknown_workflow_video_lora_sampler_357
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.859
common_nodes: [LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1ditto视频风格转绘_1981590967713185793.json, 平台全量/视频一句话转画风_2059234925508911105.json, 平台全量/视频风格转绘（吉卜力风格）_1985744669143379969.json, 平台全量/（20多种风格）Wan2.1 Ditto视频风格转绘加速版V2（KJ版）_1980270596166737921.json, 平台全量/（20多种风格）Wan2.1 Ditto视频风格转绘（KJ版）_1980267922918694913.json, 平台全量/（卡通变真人）Wan2.1 Ditto视频风格转绘（KJI版）_1980318107703160834.json, 平台全量/（（自用）-卡通变真人）Wan2.1 Ditto视频风格转绘（KJ版）_1980325810190114817.json, 数字人/数字人/视频一句话转画风_1980290599200972802.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_357

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Wan2.1ditto视频风格转绘_1981590967713185793.json、平台全量/视频一句话转画风_2059234925508911105.json、平台全量/视频风格转绘（吉卜力风格）_1985744669143379969.json、平台全量/（20多种风格）Wan2.1 Ditto视频风格转绘加速版V2（KJ版）_1980270596166737921.json、平台全量/（20多种风格）Wan2.1 Ditto视频风格转绘（KJ版）_1980267922918694913.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 7/8 个有
- `CR Prompt Text` —— 6/8 个有
- `JWInteger` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `ImageConcatMulti` —— 5/8 个有
- `WanVideoSLG` —— 4/8 个有
- `Int` —— 3/8 个有
- `PDIMAGE_LongerSize` —— 3/8 个有
- `ImageConcanate` —— 2/8 个有
- `TextInputBasic` —— 2/8 个有
- `SaveImage` —— 1/8 个有
- `TT_img_enc` —— 1/8 个有
- `TT_img_enc_v2` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
