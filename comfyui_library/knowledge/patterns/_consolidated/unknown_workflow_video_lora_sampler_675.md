---
name: unknown_workflow_video_lora_sampler_675
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84675
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, SAM3_VideoTrack, SCAIL2FitVideo, SCAIL2ReferencePack, SCAIL2ReferenceSAMBuilder, SCAIL2SimpleVideo, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/SCAIL2-多参考角色-迁移替换-4k极速流_2081364495305363458.json, 平台全量/Scail2-动作迁移-高质量多图参考版本-远景细节、重打光_2082044731672055810.json, 平台全量/scail2-动作迁移、人物替换、单人_多人_多图_2079857608680366082.json, 平台全量/scail2-多功能极简流_2077937753593040897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_675

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/SCAIL2-多参考角色-迁移替换-4k极速流_2081364495305363458.json、平台全量/Scail2-动作迁移-高质量多图参考版本-远景细节、重打光_2082044731672055810.json、平台全量/scail2-动作迁移、人物替换、单人_多人_多图_2079857608680366082.json、平台全量/scail2-多功能极简流_2077937753593040897.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SAM3_VideoTrack`
- `SCAIL2FitVideo`
- `SCAIL2ReferencePack`
- `SCAIL2ReferenceSAMBuilder`
- `SCAIL2SimpleVideo`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 2/4 个有
- `easy int` —— 2/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
