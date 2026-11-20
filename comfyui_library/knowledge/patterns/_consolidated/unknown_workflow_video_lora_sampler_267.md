---
name: unknown_workflow_video_lora_sampler_267
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7567
common_nodes: [CR Text, GetNode, JWInteger, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Primitive integer [Crystools], SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/wan2.2文生视频超级加速+TTS_2020755139161759746.json, 平台全量/wan2.2文生视频超级加速+TTS_2021452005880893442.json, 视频生成/文生视频/wan2.2图生视频V3.0（4步加速lora+kj版本）_1954108847948480514.json, 视频生成/文生视频/wan2.2文生视频V3.0（4步加速lora+kj版本）_1954108894912114689.json, 视频生成/文生视频/wan2.2文生视频超级加速——飞翔荷兰人_1971154804091326465.json, 视频生成/文生视频/wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417.json, 视频生成/文生视频/【2倍提速】Wan2.2+14B Seko 4步加速文生视频v1_1954103661171503106.json, 视频生成/文生视频/【KJ版】Wan2.2 14B加速文生视频-智能扩写提示词_1950844539659550722.json, 视频生成/文生视频/【KJ版】Wan2.2+14B 4步加速文生视频-智能扩写版_1953642911277744130.json, 视频生成/文生视频/【KJ版】Wan2.2+14B Seko Lora 4步加速文生视频-智能扩写版v2_1954106485791977474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_267

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/wan2.2文生视频超级加速+TTS_2020755139161759746.json、平台全量/wan2.2文生视频超级加速+TTS_2021452005880893442.json、视频生成/文生视频/wan2.2图生视频V3.0（4步加速lora+kj版本）_1954108847948480514.json、视频生成/文生视频/wan2.2文生视频V3.0（4步加速lora+kj版本）_1954108894912114689.json、视频生成/文生视频/wan2.2文生视频超级加速——飞翔荷兰人_1971154804091326465.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
- `CR Text`
- `GetNode`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FloatToSigmas` —— 9/10 个有
- `StringToFloatList` —— 9/10 个有
- `WanVideoEmptyEmbeds` —— 9/10 个有
- `RH_LLMAPI_NODE` —— 5/10 个有
- `ImpactSwitch` —— 4/10 个有
- `Text Concatenate` —— 4/10 个有
- `Wan22PromptSelector` —— 4/10 个有
- `WanVideoContextOptions` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `Qwen3TTSModelLoader` —— 2/10 个有
- `Qwen3TTSVoiceDesign` —— 2/10 个有
- `SaveAudio` —— 2/10 个有
- `CreateCFGScheduleFloatList` —— 1/10 个有
- `CreateVideo` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `PreViewVideo` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `WanVideoImageToVideoEncode` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
