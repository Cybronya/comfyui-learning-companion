---
name: unknown_workflow_video_sampler_unet_34
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.686667
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, GetNode, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3导演台_2061378483611328514.json, 视频生成/图生视频/【Work-Fisher】全自动六宫格LTX2.3导演台_2062044647668666370.json, 视频生成/图生视频/万象+rh四宫格横屏1280导演台自动化工作流(固定12秒插件已修复0624）_2071108486670409729.json, 视频生成/图生视频/万象+rh四宫格横屏1280导演台自动化工作流(固定12秒插件已修复0624）_2074501532183252993.json, 视频生成/图生视频/万象+rh四宫格横屏1280导演台自动化工作流_2068593388110307330.json, 视频生成/图生视频/全能图片G Image2 + LTX+2.3 Director 6宫格-片段 自动提示词 视频生成工作流_2063834779862257665.json, 视频生成/图生视频/六宫格横屏1280导演台自动化工作流（固定15秒）_2070323766567194626.json, 视频生成/图生视频/短剧漫剧wan+九宫格横屏1280导演台自动化工作流（固定20秒）_2080658867448541185.json, 视频生成/文生视频/万象+rh九宫格横屏1280导演台自动化工作流（固定18秒）_2067903674852134913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_34

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/ltx2.3导演台_2061378483611328514.json、视频生成/图生视频/【Work-Fisher】全自动六宫格LTX2.3导演台_2062044647668666370.json、视频生成/图生视频/万象+rh四宫格横屏1280导演台自动化工作流(固定12秒插件已修复0624）_2071108486670409729.json、视频生成/图生视频/万象+rh四宫格横屏1280导演台自动化工作流(固定12秒插件已修复0624）_2074501532183252993.json、视频生成/图生视频/万象+rh四宫格横屏1280导演台自动化工作流_2068593388110307330.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `PreviewAny` —— 8/9 个有
- `RH_LLMAPI_Pro_Node` —— 8/9 个有
- `TTResolutionSelector` —— 7/9 个有
- `LoadVideo` —— 6/9 个有
- `Text Multiline` —— 6/9 个有
- `LTXDirectorGuide` —— 5/9 个有
- `CS-LTXGridDirector` —— 4/9 个有
- `SF-LTXDirectorGuide` —— 4/9 个有
- `SF-LTXGridDirector` —— 4/9 个有
- `Label (rgthree)` —— 2/9 个有
- `DiffusionModelLoaderKJ` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `LTXDirector` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_RhartImageG2ImageToImage` —— 1/9 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/9 个有
- `RH_RhartImageG2OfficialTextToImage` —— 1/9 个有
- `SaveImage` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
