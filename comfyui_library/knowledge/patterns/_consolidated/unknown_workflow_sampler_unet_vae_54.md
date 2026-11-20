---
name: unknown_workflow_sampler_unet_vae_54
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.773733
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/图生图/MSR六宫格LTX2.3导演台_2072988146970742785.json, 图片生成/图生图/【Work-Fisher】全自动六宫格LTX2.3导演台_2073426994209050626.json, 平台全量/LTX2.3-导演分镜节点2.0-参考视频生成_2071062549084327938.json, 平台全量/LTX2.3-导演分镜节点2.0-视频延长_2071060329731280897.json, 平台全量/LTX2.3-导演分镜节点2.0-视频编辑（局部重绘）_2070872825044488194.json, 视频生成/图生视频/LTX+2.3 Director 6宫格 _ 单图 简化版工作流-用于集成_2064037629812895745.json, 视频生成/图生视频/LTX2.3-图生视频+导演分镜节点2.0_2070497842334097410.json, 视频生成/图生视频/LTX2.3-图生视频+导演分镜节点_2055988767751720962.json, 视频生成/图生视频/LTX2.3-图生视频+导演分镜节点（自定义音频版）_2056019458614931458.json, 视频生成/图生视频/LTX2.3-自动剧情-全自动宫格导演台_2068587096239071233.json, 视频生成/图生视频/LTX导演台_2075025517912346625.json, 视频生成/图生视频/aidir-LTX2.3-LTX Director-全自动宫格导演台-自动剧情_2070124907555545090.json, 视频生成/图生视频/aidir-LTX2.3-LTX Director-六宫格全自动宫格导演台-自动剧情_2070402488083238913.json, 视频生成/图生视频/【Work-Fisher】全自动六宫格LTX2.3导演台_2062044647668666370.json, 视频生成/图生视频/全自动六宫格LTX2.3导演台（短剧使用）_2071479057736355841.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_54

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/MSR六宫格LTX2.3导演台_2072988146970742785.json、图片生成/图生图/【Work-Fisher】全自动六宫格LTX2.3导演台_2073426994209050626.json、平台全量/LTX2.3-导演分镜节点2.0-参考视频生成_2071062549084327938.json、平台全量/LTX2.3-导演分镜节点2.0-视频延长_2071060329731280897.json、平台全量/LTX2.3-导演分镜节点2.0-视频编辑（局部重绘）_2070872825044488194.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `LoadImage` —— 10/15 个有
- `VHS_VideoCombine` —— 10/15 个有
- `CS-LTXGridDirector` —— 9/15 个有
- `GetNode` —— 9/15 个有
- `SetNode` —— 9/15 个有
- `easy cleanGpuUsed` —— 9/15 个有
- `PreviewAny` —— 8/15 个有
- `RH_LLMAPI_Pro_Node` —— 8/15 个有
- `LTXDirector` —— 7/15 个有
- `CreateVideo` —— 6/15 个有
- `PathchSageAttentionKJ` —— 6/15 个有
- `SaveVideo` —— 6/15 个有
- `TTResolutionSelector` —— 6/15 个有
- `Fast Groups Bypasser (rgthree)` —— 5/15 个有
- `ModelPreviewOverrideKJ` —— 4/15 个有
- `Int` —— 3/15 个有
- `JjkText` —— 3/15 个有
- `RH_Utils` —— 3/15 个有
- `ttN concat` —— 3/15 个有
- `孤海注释` —— 3/15 个有
- `ComfySwitchNode` —— 2/15 个有
- `LiconMSR` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
