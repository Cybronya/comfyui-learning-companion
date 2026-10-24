---
name: unknown_workflow_lora_sampler_unet_317
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9695
common_nodes: [BasicScheduler, CFGGuider, CR Text, CS-LTXGridDirector, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, Label (rgthree), LoadImage, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VRAM_Debug]
problems: []
missing: []
members: [视频生成/图生视频/魔改 LTX2.3 导演台 全自动六宫格，短剧广告动漫一键成片_2064230984832339970.json, 视频生成/图生视频/魔改 LTX2.3 导演台🔥全自动六宫格，短剧广告动漫一键成片_2063178512995020802.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_317

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/魔改 LTX2.3 导演台 全自动六宫格，短剧广告动漫一键成片_2064230984832339970.json、视频生成/图生视频/魔改 LTX2.3 导演台🔥全自动六宫格，短剧广告动漫一键成片_2063178512995020802.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CR Text`
- `CS-LTXGridDirector`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VRAM_Debug`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 1/2 个有
- `SaveMP4` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
