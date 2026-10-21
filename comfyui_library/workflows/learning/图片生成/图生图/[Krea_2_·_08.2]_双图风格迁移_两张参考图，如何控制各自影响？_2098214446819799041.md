---
key: 图片生成/图生图/[Krea_2_·_08.2]_双图风格迁移_两张参考图，如何控制各自影响？_2098214446819799041.json
name: [Krea_2_·_08.2]_双图风格迁移_两张参考图，如何控制各自影响？_2098214446819799041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/[Krea_2_·_08.2]_双图风格迁移_两张参考图，如何控制各自影响？_2098214446819799041.json
hash: fc0961f2fe557934
coverage: 0.535714
learned_at: 2026-10-21 00:45:04
nodes: [GetNode, Anything Everywhere, GetNode, GetNode, GetNode, SetNode, Krea2TwoStyleReferences, GetNode, CLIPLoader, ConditioningZeroOut, VAELoader, CLIPTextEncode, KSampler, Krea2SizePreset, GetNode, SetNode, Krea2StyleReference, SetNode, SetNode, LoadImage, UNETLoader, Krea2StyleReference, PreviewImage, LoadImage, VAEDecode, SaveImage, Krea2TwoStyleTransfer, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 712231581630102, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/[Krea_2_·_08.2]_双图风格迁移_两张参考图，如何控制各自影响？_2098214446819799041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/[Krea_2_·_08.2]_双图风格迁移_两张参考图，如何控制各自影响？_2098214446819799041.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（28 个）：
- `GetNode`
- `Anything Everywhere`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Krea2TwoStyleReferences`
- `GetNode`
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Krea2SizePreset`
- `GetNode`
- `SetNode`
- `Krea2StyleReference`
- `SetNode`
- `SetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `Krea2StyleReference`
- `PreviewImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Krea2TwoStyleTransfer`
- `MarkdownNote`

## 关键参数

- `seed` = `712231581630102`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（15/28）

**有卡**：`Krea2TwoStyleReferences`、`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`Krea2SizePreset`、`Krea2StyleReference`、`LoadImage`、`UNETLoader`、`VAEDecode`、`SaveImage`、`Krea2TwoStyleTransfer`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
