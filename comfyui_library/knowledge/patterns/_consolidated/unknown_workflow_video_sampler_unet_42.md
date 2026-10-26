---
name: unknown_workflow_video_sampler_unet_42
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.940143
common_nodes: [BasicScheduler, DualCLIPLoader, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, SamplerCustom, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ, YusuLTXDirector, YusuLTXDirectorGuide]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-MSR全能参考V2（一致性、稳定性提升）_2076860674927579138.json, 视频生成/图生视频/LTX2.3-MSR全能参考V2（一致性、稳定性提升）_2077473064631230466.json, 视频生成/图生视频/LTX2.3-导演台2.0，全新升级_2079871871297875970.json, 视频生成/图生视频/LTX2.3-导演台2.0，全新升级，多功能支持！_2070426873351467010.json, 视频生成/文生视频/LTX2.3-MSR全能参考V2（一致性、稳定性提升）_2077330675799252994.json, 视频生成/文生视频/LTX2.3-导演台2.0视频合成图生视频编辑全能视频生成_2073674326481657857.json, 视频生成/文生视频/LTX2.3-（导演台）实现各种复杂运镜方式_2072576891915165697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_42

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-MSR全能参考V2（一致性、稳定性提升）_2076860674927579138.json、视频生成/图生视频/LTX2.3-MSR全能参考V2（一致性、稳定性提升）_2077473064631230466.json、视频生成/图生视频/LTX2.3-导演台2.0，全新升级_2079871871297875970.json、视频生成/图生视频/LTX2.3-导演台2.0，全新升级，多功能支持！_2070426873351467010.json、视频生成/文生视频/LTX2.3-MSR全能参考V2（一致性、稳定性提升）_2077330675799252994.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `YusuLTXDirector`
- `YusuLTXDirectorGuide`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 6/7 个有
- `ModelPreviewOverrideKJ` —— 6/7 个有
- `LiconMSR` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `Label (rgthree)` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `YusuLTXDirectorCropGuides` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `LTXVCropGuides` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `easy int` —— 3/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
