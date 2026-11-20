---
name: unknown_workflow_lora_sampler_vae_5
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.962133
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, KSamplerSelect, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3导演分镜流_2073321199618314242.json, 平台全量/电商 多场景带货 本地_云端 都可以跑_2056647637520183298.json, 数字人/数字人/AI脱口秀_2064723957512757249.json, 数字人/数字人/AI脱口秀_2066018894162255874.json, 视频生成/图生视频/LTX 2.3直出TVC广告 娱乐版_2055655934248144898.json, 视频生成/图生视频/LTX2.3 全能导演分镜-更强的控制性_2055524487839404034.json, 视频生成/图生视频/LTX2.3全流程导演台！_2056659960074956802.json, 视频生成/图生视频/LTX2.3导演AI版的剪映版全能控制台-运镜分镜一网打进_2055283011867947010.json, 视频生成/图生视频/LTX2.3导演分镜工作流（支持多图+多个音频）自由编辑_2055157039688634370.json, 视频生成/图生视频/LTX2.3导演分镜流V2_2059815779062865922.json, 视频生成/图生视频/LTX2.3导演台工作流、短剧多分镜编辑合并、多人对口型 、数字人唱歌_2057726231881281537.json, 视频生成/图生视频/LTX导演台工作流_2055076989958139906.json, 视频生成/图生视频/LTX导演工作流-参考音频版数字人_2055639215265861633.json, 视频生成/图生视频/图片+音频多参生视频——Ltx2.3 All In One 导演级操控_2055531778017906689.json, 视频生成/文生视频/LTX2.3导演台 数字人唱歌 短剧自动切分镜 对口型工作流_2057085762369314818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_5

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/LTX2.3导演分镜流_2073321199618314242.json、平台全量/电商 多场景带货 本地_云端 都可以跑_2056647637520183298.json、数字人/数字人/AI脱口秀_2064723957512757249.json、数字人/数字人/AI脱口秀_2066018894162255874.json、视频生成/图生视频/LTX 2.3直出TVC广告 娱乐版_2055655934248144898.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 14/15 个有
- `SaveVideo` —— 14/15 个有
- `DualCLIPLoader` —— 13/15 个有
- `LTXDirector` —— 13/15 个有
- `VAELoaderKJ` —— 13/15 个有
- `CheckpointLoaderSimple` —— 12/15 个有
- `LTX2SamplingPreviewOverride` —— 10/15 个有
- `LTXVLatentUpsampler` —— 10/15 个有
- `LatentUpscaleModelLoader` —— 10/15 个有
- `ImpactSwitch` —— 4/15 个有
- `DiffusionModelLoaderKJ` —— 3/15 个有
- `Int` —— 3/15 个有
- `TTResolutionSelector` —— 3/15 个有
- `VHS_VideoCombine` —— 3/15 个有
- `ComfySwitchNode` —— 2/15 个有
- `LTXAVTextEncoderLoader` —— 2/15 个有
- `LTXVAudioVAELoader` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `LoadImage` —— 2/15 个有
- `PrimitiveBoolean` —— 2/15 个有
- `Yusu-LTXDirector` —— 2/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
