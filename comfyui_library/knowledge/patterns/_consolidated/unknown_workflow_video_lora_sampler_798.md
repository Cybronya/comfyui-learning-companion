---
name: unknown_workflow_video_lora_sampler_798
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.905667
common_nodes: [ImageResizeKJv2, Int, LoadWanVideoT5TextEncoder, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.1文生视频+视频转绘_1949717734896082946.json, 平台全量/Ditto视频转绘工作流_1981174661876695042.json, 视频生成/图生视频/Wan2.1图生视频+视频转绘_1949722105333075970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_798

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Wan2.1文生视频+视频转绘_1949717734896082946.json、平台全量/Ditto视频转绘工作流_1981174661876695042.json、视频生成/图生视频/Wan2.1图生视频+视频转绘_1949722105333075970.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResizeKJv2`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `WanVideoApplyNAG` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `WanVideoTextEncodeSingle` —— 2/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `WanVideoSLG` —— 1/3 个有
- `WanVideoTextEncode` —— 1/3 个有
- `WanVideoVACEModelSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
