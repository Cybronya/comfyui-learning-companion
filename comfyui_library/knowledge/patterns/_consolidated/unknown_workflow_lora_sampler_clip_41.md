---
name: unknown_workflow_lora_sampler_clip_41
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 1
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2FitVideo, SCAIL2SimpleVideo, VAELoader, VHS_LoadVideo, WanChunkFeedForward]
problems: []
missing: []
members: [视频生成/图生视频/Ai 数字人_2086011335233589249.json, 视频生成/图生视频/2064999318582546433.json, 视频生成/图生视频/SCAIL2动作模型跳舞模仿带货视频人物替换短剧视频角色替换_2083912499828715522.json, 视频生成/图生视频/SCAIL2超强一致性动作迁移_2085596899859582977.json, 视频生成/图生视频/SCAIL2超强一致性动作迁移_2086658199561789442.json, 视频生成/图生视频/SCAIL2超强一致性动作迁移_2087087255763644418.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Ai 数字人_2086011335233589249.json、视频生成/图生视频/2064999318582546433.json、视频生成/图生视频/SCAIL2动作模型跳舞模仿带货视频人物替换短剧视频角色替换_2083912499828715522.json、视频生成/图生视频/SCAIL2超强一致性动作迁移_2085596899859582977.json、视频生成/图生视频/SCAIL2超强一致性动作迁移_2086658199561789442.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2FitVideo`
- `SCAIL2SimpleVideo`
- `VAELoader`
- `VHS_LoadVideo`
- `WanChunkFeedForward`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 5/6 个有
- `Int` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `ComfySwitchNodeV2` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `RH_HeyGemNode` —— 1/6 个有
- `SaveVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
