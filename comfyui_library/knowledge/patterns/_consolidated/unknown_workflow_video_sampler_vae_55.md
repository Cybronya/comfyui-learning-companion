---
name: unknown_workflow_video_sampler_vae_55
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.652667
common_nodes: [GetImageSizeAndCount, GetNode, ImageResizeKJ, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/万象VACE 14B视频扩展-加速版_1923359866998411265.json, 视频生成/图生视频/万象VACE 14B视频驱动图片-加速版_1923351461173129217.json, 视频生成/图生视频/万象加速时代-ACCVID_1927701391375253506.json, 视频生成/图生视频/最新Wan2.1+Vace  视频画面内容拓展【中文注释简单易懂】_1911760861873274882.json, 视频生成/图生视频/最新Wan2.1+Vace首尾帧  极速运行 中文注释_1912169450282647553.json, 视频生成/图生视频/视频动作迁移｜上传视频和图片｜深度+open pose 控制_1937838882719469569.json, 视频生成/图生视频/通义万相最新VACE超级无限循环首尾帧图生视频_1908024871404904449.json, 视频生成/图生视频/通义万相统一模型FusionX-LORA版本美女跳舞转绘工作流_1935676000963321857.json, 视频生成/文生视频/wan2.1 极速动作模仿 动作迁移 跳舞_1925016376795144194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_55

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/万象VACE 14B视频扩展-加速版_1923359866998411265.json、视频生成/图生视频/万象VACE 14B视频驱动图片-加速版_1923351461173129217.json、视频生成/图生视频/万象加速时代-ACCVID_1927701391375253506.json、视频生成/图生视频/最新Wan2.1+Vace  视频画面内容拓展【中文注释简单易懂】_1911760861873274882.json、视频生成/图生视频/最新Wan2.1+Vace首尾帧  极速运行 中文注释_1912169450282647553.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 9 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoVACEModelSelect` —— 8/9 个有
- `LoadImage` —— 7/9 个有
- `VHS_LoadVideo` —— 7/9 个有
- `WanVideoExperimentalArgs` —— 7/9 个有
- `WanVideoSLG` —— 7/9 个有
- `AddLabel` —— 6/9 个有
- `EmptyImage` —— 6/9 个有
- `ImageConcatMulti` —— 6/9 个有
- `WanVideoLoraSelect` —— 6/9 个有
- `WanVideoTorchCompileSettings` —— 6/9 个有
- `AIO_Preprocessor` —— 5/9 个有
- `WanVideoTeaCache` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `ImagePadKJ` —— 4/9 个有
- `MaskPreview+` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `ColorMatch` —— 3/9 个有
- `Primitive integer [Crystools]` —— 3/9 个有
- `Text Concatenate` —— 3/9 个有
- `Text Multiline` —— 3/9 个有
- `GetImageRangeFromBatch` —— 2/9 个有
- `INTConstant` —— 2/9 个有
- `ImageBlend` —— 2/9 个有
- `RH_Captioner` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `WanVideoVACEStartToEndFrame` —— 2/9 个有
- `DWPreprocessor` —— 1/9 个有
- `ImageBatch` —— 1/9 个有
- `WanVideoVRAMManagement` —— 1/9 个有
- `Zoe-DepthMapPreprocessor` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
