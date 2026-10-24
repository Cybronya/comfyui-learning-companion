---
name: unknown_workflow_sampler_unet_vae_182
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.980167
common_nodes: [BasicGuider, CLIPLoader, CreateVideo, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3VDNExecutionPlanT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/02_MiniMax H3｜OpenVDN DMD8｜通用生视频 768P_2099156575138177025.json, 视频生成/文生视频/MiniMax H3｜OpenVDN DMD8 深度视频引导视频生成｜动作·运镜·结构迁移_2103416786740924418.json, 视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜参考生视频_2098317972656971777.json, 视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜参考生视频_2099120747452129282.json, 视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜通用生视频 2K_2098414505846992898.json, 视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜通用生视频 4K_2098414520787103746.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_182

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/02_MiniMax H3｜OpenVDN DMD8｜通用生视频 768P_2099156575138177025.json、视频生成/文生视频/MiniMax H3｜OpenVDN DMD8 深度视频引导视频生成｜动作·运镜·结构迁移_2103416786740924418.json、视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜参考生视频_2098317972656971777.json、视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜参考生视频_2099120747452129282.json、视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜通用生视频 2K_2098414505846992898.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
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
- `RH_DLSS5FrameInterpolation` —— 3/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `Int` —— 2/6 个有
- `SeedVR2` —— 2/6 个有
- `SeedVR2BlockSwap` —— 2/6 个有
- `GetVideoComponents` —— 1/6 个有
- `LoadVideo` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `Video Slice` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
