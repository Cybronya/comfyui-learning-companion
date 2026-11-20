---
name: unknown_workflow_video_lora_sampler_375
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.69
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/全自动四宫格LTX2.3导演台_2068160315895934977.json, 视频生成/文生视频/万象+rh九宫格横屏1280导演台自动化工作流（固定20秒）_2069405147431792641.json, 视频生成/文生视频/万象+rh九宫格横屏1280导演台自动化工作流（固定20秒）_2074632138728763394.json, 视频生成/文生视频/万象+rh六宫格横屏1280导演台自动化工作流（固定15秒）_2069737985674928129.json, 视频生成/文生视频/万象+rh四宫格横屏1280导演台自动化工作流(固定12秒插件已修复0624）_2066856869905395714.json, 视频生成/文生视频/万象+rh四宫格竖屏1280导演台自动化工作流(固定12秒插件0707）_2074626267659456513.json, 视频生成/文生视频/全自动多宫格LTX2.3导演台+光锥多参生视频(0623修复）_2066670452965199873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_375

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/全自动四宫格LTX2.3导演台_2068160315895934977.json、视频生成/文生视频/万象+rh九宫格横屏1280导演台自动化工作流（固定20秒）_2069405147431792641.json、视频生成/文生视频/万象+rh九宫格横屏1280导演台自动化工作流（固定20秒）_2074632138728763394.json、视频生成/文生视频/万象+rh六宫格横屏1280导演台自动化工作流（固定15秒）_2069737985674928129.json、视频生成/文生视频/万象+rh四宫格横屏1280导演台自动化工作流(固定12秒插件已修复0624）_2066856869905395714.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `TTResolutionSelector` —— 6/7 个有
- `LoadVideo` —— 5/7 个有
- `Text Multiline` —— 5/7 个有
- `SF-LTXDirectorGuide` —— 4/7 个有
- `SF-LTXGridDirector` —— 4/7 个有
- `CS-LTXDirectorGuide` —— 3/7 个有
- `CS-LTXGridDirector` —— 3/7 个有
- `Label (rgthree)` —— 2/7 个有
- `ImpactSwitch` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
