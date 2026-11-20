---
name: unknown_workflow_sampler_unet_vae_269
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9472
common_nodes: [BasicGuider, CLIPLoader, CreateVideo, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3VDNExecutionPlanT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [平台全量/MiniMax H3 视频编辑：视频翻拍、二创与指定角色替换_2105277473796747266.json, 视频生成/文生视频/02_MiniMax H3｜OpenVDN DMD8｜通用生视频 768P_2099156575138177025.json, 视频生成/文生视频/MiniMax H3｜OpenVDN DMD8 深度视频引导视频生成｜动作·运镜·结构迁移_2103416786740924418.json, 视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜参考生视频_2098317972656971777.json, 视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜参考生视频_2099120747452129282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_269

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/MiniMax H3 视频编辑：视频翻拍、二创与指定角色替换_2105277473796747266.json、视频生成/文生视频/02_MiniMax H3｜OpenVDN DMD8｜通用生视频 768P_2099156575138177025.json、视频生成/文生视频/MiniMax H3｜OpenVDN DMD8 深度视频引导视频生成｜动作·运镜·结构迁移_2103416786740924418.json、视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜参考生视频_2098317972656971777.json、视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜参考生视频_2099120747452129282.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CreateVideo`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 2/5 个有
- `LoadVideo` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `Video Slice` —— 2/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `RH_DLSS5FrameInterpolation` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
