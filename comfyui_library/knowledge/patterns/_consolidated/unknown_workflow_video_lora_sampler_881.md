---
name: unknown_workflow_video_lora_sampler_881
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.948333
common_nodes: [CR Text Concatenate, ColorMatch, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, RH_Translator, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Self-Forcing-VACE极速版-VACE 14B图生视频_1934433981473452033.json, 视频生成/图生视频/wan2.1-fusionx系列极速完美复刻迁移动作_1937759191832662018.json, 视频生成/图生视频/（VACE-14B系列）动作迁移Causvid加速_1932804540896792578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_881

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Self-Forcing-VACE极速版-VACE 14B图生视频_1934433981473452033.json、视频生成/图生视频/wan2.1-fusionx系列极速完美复刻迁移动作_1937759191832662018.json、视频生成/图生视频/（VACE-14B系列）动作迁移Causvid加速_1932804540896792578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text Concatenate`
- `ColorMatch`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RH_Translator`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `WanVideoMagCache` —— 1/3 个有
- `WanVideoVACEStartToEndFrame` —— 1/3 个有
- `easy textSwitch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
