---
name: unknown_workflow_video_lora_sampler_609
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9252
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MoviiGen 3倍加速超强微动态图生视频V2_1924658376096346114.json, 视频生成/图生视频/MoviiGen+Vace14B图生视频加速版_1928040870858375169.json, 视频生成/图生视频/MoviiGen超强动作细节表达高清文生视频优化版_1924759353528938497.json, 视频生成/图生视频/VACE CausVid ( Lora ) - 3~5倍加速-图生视频_1923698018254508033.json, 视频生成/图生视频/VACE14B+CausVid+骨骼图控制视频转绘_1925394703754403841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_609

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MoviiGen 3倍加速超强微动态图生视频V2_1924658376096346114.json、视频生成/图生视频/MoviiGen+Vace14B图生视频加速版_1928040870858375169.json、视频生成/图生视频/MoviiGen超强动作细节表达高清文生视频优化版_1924759353528938497.json、视频生成/图生视频/VACE CausVid ( Lora ) - 3~5倍加速-图生视频_1923698018254508033.json、视频生成/图生视频/VACE14B+CausVid+骨骼图控制视频转绘_1925394703754403841.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `TextInput_`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `WanVideoVACEStartToEndFrame` —— 4/5 个有
- `ImageRepeat` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `ImageResizeKJ` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `WanVideoTeaCache` —— 2/5 个有
- `DWPreprocessor` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImagePadKJ` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `PDIMAGE_LongerSize` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy imageSize` —— 1/5 个有
- `ttN int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
